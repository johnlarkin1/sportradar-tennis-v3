from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_competitor_merge_mappings_locale import GetCompetitorMergeMappingsLocale
from ...models.get_competitor_merge_mappings_response_200 import GetCompetitorMergeMappingsResponse200
from ...types import Response


def _get_kwargs(
    locale: GetCompetitorMergeMappingsLocale,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/competitors/merge_mappings" + f".{format}",  # Append format to URL
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetCompetitorMergeMappingsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCompetitorMergeMappingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetCompetitorMergeMappingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetCompetitorMergeMappingsLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetCompetitorMergeMappingsResponse200]:
    """Get old and new IDs of players that have been merged

     Get old and new IDs of players that have been merged

    Args:
        locale (GetCompetitorMergeMappingsLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompetitorMergeMappingsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetCompetitorMergeMappingsLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetCompetitorMergeMappingsResponse200]:
    """Get old and new IDs of players that have been merged

     Get old and new IDs of players that have been merged

    Args:
        locale (GetCompetitorMergeMappingsLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompetitorMergeMappingsResponse200
    """

    return sync_detailed(
        locale=locale,
        client=client,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetCompetitorMergeMappingsLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetCompetitorMergeMappingsResponse200]:
    """Get old and new IDs of players that have been merged

     Get old and new IDs of players that have been merged

    Args:
        locale (GetCompetitorMergeMappingsLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompetitorMergeMappingsResponse200]
    """

    kwargs = _get_kwargs(locale=locale, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetCompetitorMergeMappingsLocale,
    *,
    client: AuthenticatedClient,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetCompetitorMergeMappingsResponse200]:
    """Get old and new IDs of players that have been merged

     Get old and new IDs of players that have been merged

    Args:
        locale (GetCompetitorMergeMappingsLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompetitorMergeMappingsResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            client=client,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
