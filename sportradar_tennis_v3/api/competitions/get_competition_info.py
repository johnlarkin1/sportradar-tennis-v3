from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_competition_info_locale import GetCompetitionInfoLocale
from ...models.get_competition_info_response_200 import GetCompetitionInfoResponse200
from ...types import Response


def _get_kwargs(
    locale: GetCompetitionInfoLocale,
    urn_competition: str,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/competitions/{urn_competition}/info" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetCompetitionInfoResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCompetitionInfoResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetCompetitionInfoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetCompetitionInfoLocale,
    urn_competition: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetCompetitionInfoResponse200]:
    """info for a competition

     info for a competition

    Args:
        locale (GetCompetitionInfoLocale):
        urn_competition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompetitionInfoResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_competition=urn_competition, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetCompetitionInfoLocale,
    urn_competition: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetCompetitionInfoResponse200]:
    """info for a competition

     info for a competition

    Args:
        locale (GetCompetitionInfoLocale):
        urn_competition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompetitionInfoResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_competition=urn_competition,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetCompetitionInfoLocale,
    urn_competition: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetCompetitionInfoResponse200]:
    """info for a competition

     info for a competition

    Args:
        locale (GetCompetitionInfoLocale):
        urn_competition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompetitionInfoResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_competition=urn_competition, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetCompetitionInfoLocale,
    urn_competition: str,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetCompetitionInfoResponse200]:
    """info for a competition

     info for a competition

    Args:
        locale (GetCompetitionInfoLocale):
        urn_competition (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompetitionInfoResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_competition=urn_competition,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
