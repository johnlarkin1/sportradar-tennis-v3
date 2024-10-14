from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_competitor_profile_locale import GetCompetitorProfileLocale
from ...types import Response


def _get_kwargs(
    locale: GetCompetitorProfileLocale,
    urn_competitor: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/competitors/{urn_competitor}/profile",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetCompetitorProfileLocale,
    urn_competitor: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """get information and players for a competitor

     Get information and players for the given urn.

    Args:
        locale (GetCompetitorProfileLocale):
        urn_competitor (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_competitor=urn_competitor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetCompetitorProfileLocale,
    urn_competitor: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """get information and players for a competitor

     Get information and players for the given urn.

    Args:
        locale (GetCompetitorProfileLocale):
        urn_competitor (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_competitor=urn_competitor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
